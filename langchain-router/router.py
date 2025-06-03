import asyncio
from llm_client import LLMClient

# Instantiate clients for your different models
lexi = LLMClient(model_name="lexi-uncensored")
deepseek = LLMClient(model_name="deepseek-coder")
nous_hermes = LLMClient(model_name="nous-hermes")

# Track loaded models for lazy loading
loaded_models = set()

async def load_model_if_needed(model: LLMClient):
    if model.model_name not in loaded_models:
        await model.load()
        loaded_models.add(model.model_name)

async def unload_model(model: LLMClient):
    if model.model_name in loaded_models:
        await model.unload()
        loaded_models.remove(model.model_name)

async def route_request(user_id: str, message: str):
    # VERY basic intent detection — replace with your own logic or a classifier
    msg_lower = message.lower()

    if any(word in msg_lower for word in ["code", "script", "program", "function"]):
        await load_model_if_needed(deepseek)
        response = await deepseek.generate(message)
        return "deepseek-coder", response

    if any(word in msg_lower for word in ["exchange server", "reboot", "domain", "sysadmin", "network"]):
        await load_model_if_needed(nous_hermes)
        response = await nous_hermes.generate(message)
        return "nous-hermes", response

    # Default fallback is lexi
    await load_model_if_needed(lexi)
    response = await lexi.generate(message)
    return "lexi-uncensored", response
