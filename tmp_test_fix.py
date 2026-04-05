import sys
import os
import json
from datetime import datetime

# Add project root to sys.path
project_root = r"c:\Users\Rodolfo Olivera\Desktop\Opengravity\trendradar-repo"
sys.path.append(project_root)

from mcp_server.tools.data_query import DataQueryTools

def test_trending_topics():
    print("Testing get_trending_topics with limit and include_url...")
    tools = DataQueryTools(project_root)
    # This crashed before
    result = tools.get_trending_topics(limit=5, include_url=True)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    test_trending_topics()
