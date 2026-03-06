import random, json
from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass
class Task:
    id: int
    payload: dict


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        pass


class TaskSourceFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        if not isinstance(self, TaskSource):
            raise TypeError("Не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                tasks = [Task(id = i["id"], payload={"user_id": i["user_id"]}) for i in data]
            return tasks
        except Exception:
            raise


class TaskSourceGenerator:
    def __init__(self):
        if not isinstance(self, TaskSource):
            raise TypeError("Не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        return [Task(id = random.randint(1,101), payload = {"user_id": random.randint(100,1001), "count": random.randint(1000,10001)}) for i in range(10)]


class TaskSourceAPI:
    def __init__(self):
        if not isinstance(self, TaskSource):
            raise TypeError("Не соответствует протоколу TaskSource")

    def get_tasks(self) -> list[Task]:
        return [
            Task(id=10, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=11, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=12, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)}),
            Task(id=13, payload={"user_id": random.randint(100, 1001), "count": random.randint(1000,10001)})
        ]