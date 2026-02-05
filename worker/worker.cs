// Redis client
using StackExchange.Redis;

// PostgreSQL driver
using Npgsql;


// Connect to Redis container
var redis = ConnectionMultiplexer.Connect("redis");

// Get database object
var redisDb = redis.GetDatabase();


// PostgreSQL connection string
var connString = "Host=db;Username=postgres;Password=postgres;Database=votes";

// Connect to database
var pg = new NpgsqlConnection(connString);
pg.Open();

Console.WriteLine("Worker started... waiting for votes");


// Infinite loop to continuously process votes
while (true)
{
    // Pop one vote from Redis queue
    var vote = redisDb.ListLeftPop("votes");

    // If vote exists
    if (vote != null)
    {
        // Insert vote into PostgreSQL
        var cmd = new NpgsqlCommand(
            "INSERT INTO votes(choice) VALUES(@choice)", pg);

        cmd.Parameters.AddWithValue("choice", vote.ToString());

        cmd.ExecuteNonQuery();

        Console.WriteLine($"Stored vote: {vote}");
    }

    // Small delay to reduce CPU usage
    Thread.Sleep(200);
}
