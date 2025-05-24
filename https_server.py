import http.server
import ssl
import os

# Specify the directory where your site files (HTML, CSS, JS, etc.) are located
web_root = os.path.join(os.getcwd(), 'public')  # Adjust if your folder name is different

# Define the server address and port
server_address = ('', 8000)  # '' means to listen on all interfaces, 8000 is the port

# Create the HTTP server with custom handler
handler = http.server.SimpleHTTPRequestHandler
handler.directory = web_root  # Specify the folder to serve
httpd = http.server.HTTPServer(server_address, handler)

# Set up SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# Wrap the socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Start the server
print("🔐 HTTPS server running at https://127.0.0.1:8000")
httpd.serve_forever()
