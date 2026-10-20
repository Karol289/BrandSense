var builder = WebApplication.CreateBuilder(args);

// Ensure app binds to 0.0.0.0 inside the container
builder.WebHost.UseUrls("http://0.0.0.0:8080");

var app = builder.Build();

app.MapGet("/", () => "Backend API is online!");
app.MapGet("/health", () => Results.Ok(new { status = "Healthy", timestamp = DateTime.UtcNow }));

app.Run();