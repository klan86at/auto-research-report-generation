import importlib.metadata
packages = [
    "langgraph",
    "langchain_communtiy",
    "langchain_core",
    "tavily-python",
    "wikipedia"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")