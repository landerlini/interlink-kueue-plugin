import logging
from typing import List

from fastapi import FastAPI, HTTPException
import interlink

from kuinterlink import KueueProvider
from kuinterlink import configuration as cfg

# Initialize FastAPI app
app = FastAPI()

# Please Take my provider and handle the interLink REST layer for me
kueue_provider = KueueProvider()

log_format = '%(asctime)-22s %(name)-10s %(levelname)-8s %(message)-90s'
logging.basicConfig(
    format=log_format,
    level=logging.DEBUG if cfg.DEBUG else logging.INFO,
)
logging.debug("Enabled debug mode.")

@app.post("/create")
async def create_pod(pods: List[interlink.Pod]) -> str:
    return kueue_provider.create_pod(pods)

@app.post("/delete")
async def delete_pod(pod: interlink.PodRequest) -> str:
    return kueue_provider.delete_pod(pod)

@app.get("/status")
async def get_pod_status(pods: List[interlink.PodRequest]) -> List[interlink.PodStatus]:
    return kueue_provider.get_pod_status(pods)

@app.post("/getLogs")
async def get_pod_logs(req: interlink.LogRequest) -> bytes:
    return kueue_provider.get_logs(req)


@app.post("/healthz")
async def healtz() -> bool:
    logging.debug("Health tested: ok.")
    return True


