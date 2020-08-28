using System.Net.WebSockets;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;

namespace WebSocketServer
{
    public class Startup
    {
        
        public void ConfigureServices(IServiceCollection services)
        {
        }

        [System.Obsolete]
        public void Configure(IApplicationBuilder app, Microsoft.AspNetCore.Hosting.IHostingEnvironment env)
        {
         app.UseWebSockets();

         app.Use(async (context, next) =>
         {
             if(context.WebSockets.IsWebSocketRequest)
             {
              WebSocket webSocket = await context.WebSockets.AcceptWebSocketAsync();
                 System.Console.WriteLine("Websocket Connected");   
             }
             else
             {
                 await next();
             }
         });   
        }
    }
}