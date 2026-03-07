import random, logging
from src.models.task import Task, TaskSource

logger = logging.getLogger(__name__)


class TaskSourceGenerator:
    def __init__(self):
        if not isinstance(self, TaskSource):
            logger.error(f"{self.__class__.__name__} не соответствует протоколу TaskSource")
            raise TypeError(f"{self.__class__.__name__} не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        return [Task(id = random.randint(1,101), payload = {"user_id": random.randint(100,1001), "count": random.randint(1000,10001)}) for i in range(10)]