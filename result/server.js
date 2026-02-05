// Express = simple web server
const express = require("express")

// PostgreSQL client
const { Pool } = require("pg")

const app = express()


// Connect to Postgres container
const pool = new Pool({
  host: "db",
  user: "postgres",
  password: "postgres",
  database: "votes"
})


// When browser hits /
app.get("/", async (req, res) => {

  // Count votes grouped by choice
  const result = await pool.query(
    "SELECT choice, COUNT(*) FROM votes GROUP BY choice"
  )

  let html = "<h2>Live Results 📊</h2>"

  // Create simple HTML output
  result.rows.forEach(r => {
    html += `${r.choice}: ${r.count}<br>`
  })

  res.send(html)
})


// Start server
app.listen(80, () => console.log("Result app running"))
