from fastmcp import FastMCP
import threading, asyncio

# Initialize the server with a name
mcp = FastMCP("WeatherService")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a specific city.
    """
    # In a real app, you would call a weather API here.
    mock_data = {
        "new york": "Sunny, 72°F",
        "london": "Rainy, 44°C",
        "tokyo": "Cloudy, 22°C"
    }
    return mock_data.get(city.lower(), f"Weather data for {city} is unavailable.")

if __name__ == "__main__":
    mcp.run(transport="stdio")