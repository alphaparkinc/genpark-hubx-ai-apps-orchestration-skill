import sys, json
from client import HubXAIAppsOrchestrator

def handle_mcp():
    orchestrator = HubXAIAppsOrchestrator()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(orchestrator.run_benchmark_hubx_portfolio(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            
            if method == "initialize":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "genpark-hubx-ai-apps-orchestration-skill", "version": "1.1.0"},
                    "capabilities": {"tools": {}}
                }}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [
                    {"name": "route_hubx_app", "description": "Automatically classify and dispatch user requests to optimal HubX app.", "inputSchema": {"type": "object", "properties": {"user_prompt": {"type": "string"}}}},
                    {"name": "dispatch_nova_assistant", "description": "Execute multi-model conversational query via Nova AI.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}}},
                    {"name": "dispatch_vision_analysis", "description": "Execute botanical (PlantApp) or nutrition (Lean) vision diagnostics.", "inputSchema": {"type": "object", "properties": {"target_app": {"type": "string"}, "image_reference": {"type": "string"}}}},
                    {"name": "dispatch_generative_studio", "description": "Execute artistic generation (DaVinci), portrait styling (Momo), or home redesign (HomeAI).", "inputSchema": {"type": "object", "properties": {"target_app": {"type": "string"}, "style_spec": {"type": "object"}}}},
                    {"name": "run_benchmark_hubx_portfolio", "description": "Run comprehensive benchmark across all HubX products.", "inputSchema": {"type": "object"}}
                ]}}
            elif method == "tools/call":
                tname = req.get("params", {}).get("name")
                args = req.get("params", {}).get("arguments", {})
                if tname == "route_hubx_app":
                    res = orchestrator.route_hubx_app(args.get("user_prompt", ""))
                elif tname == "dispatch_nova_assistant":
                    res = orchestrator.dispatch_nova_assistant(args.get("query", ""))
                elif tname == "dispatch_vision_analysis":
                    res = orchestrator.dispatch_vision_analysis(args.get("target_app", "plantapp"), args.get("image_reference", ""))
                elif tname == "dispatch_generative_studio":
                    res = orchestrator.dispatch_generative_studio(args.get("target_app", "davinci"), args.get("style_spec", {}))
                else:
                    res = orchestrator.run_benchmark_hubx_portfolio()
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_mcp()
