# because of dotnet, we always build on amd64, and control target platforms via CLI
# reason: .NET has limited and unstable support for cross-architecture emulation

# dotnet doesn't support QEMU for building or running
# QEMU is used by Docker to emulate other CPU architectures (like ARM on Intel)

# errors are very common on arm/v7 (32-bit ARM)
# examples: illegal instruction, segmentation fault, runtime crashes

# ------------------------------------------------------------

# build stage
# --platform=${BUILDPLATFORM} ensures the build runs on the builder's native CPU
# this avoids QEMU emulation issues with .NET
FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:7.0 AS build

# TARGETPLATFORM = final image platform (e.g. linux/amd64, linux/arm64)
# TARGETARCH = cpu architecture only (e.g. amd64, arm64)
# BUILDPLATFORM = platform where the build is actually running
ARG TARGETPLATFORM
ARG TARGETARCH
ARG BUILDPLATFORM

# print platforms for debugging and visibility during build
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"

# set working directory inside container
WORKDIR /source

# copy only the project file first
# this allows Docker layer caching for dependency restore
COPY *.csproj .

# restore NuGet dependencies for the target architecture
# -a specifies architecture (important for multi-arch builds)
RUN dotnet restore -a $TARGETARCH

# copy remaining source code
COPY . .

# compile and publish the application
# -c release = optimized production build
# -o /app = output directory
# -a $TARGETARCH = compile for target CPU
# --self-contained false = use runtime image instead of bundling runtime
# --no-restore = avoid restoring again (already done)
RUN dotnet publish -c release -o /app -a $TARGETARCH --self-contained false --no-restore

# ------------------------------------------------------------

# runtime stage (smaller image, no SDK)
FROM mcr.microsoft.com/dotnet/runtime:7.0

# set working directory for runtime container
WORKDIR /app

# copy published output from build stage
COPY --from=build /app .

# start the .NET worker service when container starts
ENTRYPOINT ["dotnet", "Worker.dll"]
