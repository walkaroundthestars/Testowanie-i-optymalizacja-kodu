from clearml import Task
from clearml.automation import HyperParameterOptimizer, DiscreteParameterRange, UniformParameterRange

task = Task.init(project_name="CNN psy", task_name="HPO")
optimizer = HyperParameterOptimizer(
    base_task_id='5d981ef78811450c8ae4efae4e79a801',

    hyper_parameters=[
        DiscreteParameterRange("General/normalization", [False, True]),
        DiscreteParameterRange("General/augmentation", [False, True]),
        DiscreteParameterRange("General/dropout", [False, True]),
        DiscreteParameterRange("General/extra_data", [False, True]),
        DiscreteParameterRange("General/image_size", [96, 160, 224]),
        DiscreteParameterRange("General/batch_size", [32, 64, 128]),
        DiscreteParameterRange("General/model_name", ["resnet50", "vgg16", "mobilenet_v2", "inception_v3", "resnet101"]),
    ],

    objective_metric_title='Accuracy',
    objective_metric_series='Validation',
    objective_metric_sign='max',

    max_iteration=10,
    max_completed_tasks=10,
    time_between_runs=30,
    execution_queue="default",  # Twoja kolejka agentowa
    save_top_k_tasks_only=3,  # zachowaj tylko najlepsze 3
)

optimizer.set_time_limit(in_minutes=60)
optimizer.start()