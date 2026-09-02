import sys
from graph.workflow import AIFactoryResearchGraph


def main():
    print("=" * 80)
    print(" AI FACTORY GROWTH EQUITY RESEARCH SYSTEM (TAFGS ENGINE)")
    print("=" * 80)
    print("\nExecuting multi-agent state graph pipeline...\n")
    
    graph = AIFactoryResearchGraph()
    results = graph.run_full_pipeline()
    
    print("\n" + "=" * 80)
    print(" PIPELINE EXECUTION LOGS")
    print("=" * 80)
    for log in results["execution_logs"]:
        print(log)
        
    print("\n" + "=" * 80)
    print(" TOP 20 AI FACTORY GROWTH RANKING (TAFGS)")
    print("=" * 80 + "\n")
    print(results["markdown_report"])


if __name__ == "__main__":
    main()
