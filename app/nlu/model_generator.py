from typing import List

from app.database.schemas.nlu_model_registry_schema import NLURegistrySchema


class PipelineStep:
    def forward(self, text_input) -> str:
        pass


class NLUPreprocessingPipeline:

    def __init__(self, steps=List[PipelineStep]):
        self.steps = steps


    def preprocess(self, text_input:str) -> str:
        output = text_input
        for step in self.steps:
            output = step.forward(output)
        return output


class NLUEmbeddings:
    pass


class NLUModel:

    def __init__(self,
                 embeddings: NLUEmbeddings,
                 preprocessing_pipeline: NLUPreprocessingPipeline,
                 intents: List[str],
                 data: NLURegistrySchema):
        self.embeddings = embeddings
        self.pipeline = preprocessing_pipeline
        self.intents = intents
        self.data = data

    def train(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def predict(self):
        pass
