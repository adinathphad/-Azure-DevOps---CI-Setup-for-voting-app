# Official .NET SDK image
FROM mcr.microsoft.com/dotnet/sdk:8.0

WORKDIR /app

COPY . .

# Install dependencies
RUN dotnet restore

# Build optimized release version
RUN dotnet publish -c Release -o out

# Run compiled app
CMD ["dotnet", "out/worker.dll"]
