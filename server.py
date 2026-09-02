import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from graph.workflow import AIFactoryResearchGraph
from core.capital_stack import get_capital_stack_summary
from data.seed_universe import get_seed_universe

app = FastAPI(
    title="AI Factory Growth Equity Identification System",
    description="Multi-Agent LangGraph Framework for Scoring Public AI Infrastructure Equities",
    version="1.0.0"
)

# Shared in-memory cache of pipeline results
graph_engine = AIFactoryResearchGraph()
cached_results = graph_engine.run_full_pipeline()


@app.get("/api/capital-stack")
def api_capital_stack():
    """Returns the Stargate reference $60.97B capital stack allocation across 12 layers."""
    return get_capital_stack_summary()


@app.get("/api/rankings")
def api_rankings():
    """Returns the latest Top 20 AI Factory Growth Ranking leaderboard."""
    return cached_results["ranking"]


@app.get("/api/company/{ticker}")
def api_company(ticker: str):
    """Returns deep-dive evaluation details for a specific ticker."""
    top_20 = cached_results["ranking"]["top_20"]
    for item in top_20:
        if item["ticker"].upper() == ticker.upper():
            # Find original seed company data for full thesis
            seed_comp = next((c for c in get_seed_universe() if c.ticker.upper() == ticker.upper()), None)
            return {
                "evaluation": item,
                "company_details": seed_comp.model_dump() if seed_comp else None
            }
    raise HTTPException(status_code=404, detail=f"Company '{ticker}' not found in Top 20 ranking.")


@app.post("/api/run-research")
def api_run_research():
    """Triggers dynamic multi-agent research refresh and updates rankings."""
    global cached_results
    cached_results = graph_engine.run_full_pipeline()
    return {
        "status": "success",
        "message": "Research cycle executed successfully across 8 agents.",
        "execution_logs": cached_results["execution_logs"],
        "top_20_count": len(cached_results["ranking"]["top_20"])
    }


@app.get("/api/report/markdown")
def api_report_markdown():
    """Returns the formatted Markdown investor report."""
    return {"markdown": cached_results["markdown_report"]}


@app.get("/", response_class=HTMLResponse)
def index_page():
    """Serves the main interactive web dashboard."""
    html_path = os.path.join(os.path.dirname(__file__), "web", "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return HTMLResponse("<h2>AI Factory Research Backend Running. Dashboard file web/index.html not found.</h2>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
