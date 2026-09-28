from client import HubXAIAppsOrchestrator
import json

def test():
    orch = HubXAIAppsOrchestrator()
    print("=== Testing HubX AI Apps Portfolio Orchestration ===")
    
    # 1. Routing Test
    route = orch.route_hubx_app("Diagnose yellow spots on my monstera plant")
    print("\n[1] Dynamic App Routing:")
    print(json.dumps(route, indent=2))
    
    # 2. Vision Analysis
    diag = orch.dispatch_vision_analysis("plantapp", "s3://images/leaf_sample.jpg")
    print("\n[2] PlantApp Vision Diagnostic:")
    print(json.dumps(diag, indent=2))

    # 3. Portfolio Benchmark
    bench = orch.run_benchmark_hubx_portfolio()
    print("\n[3] Full Portfolio Benchmark:")
    print(json.dumps(bench, indent=2))

if __name__ == "__main__":
    test()
