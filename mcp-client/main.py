import sys

import asyncio

from client import MCPClient

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        try:
            await client.cleanup()
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)
