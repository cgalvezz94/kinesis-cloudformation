output "lambda_function_name" {
  value       = module.streaming_stack.lambda_function_name
  description = "Nombre de la función Lambda"
}

output "grafana_workspace_id" {
  value       = module.streaming_stack.grafana_workspace_id
  description = "ID del workspace de Grafana"
}

output "ecs_task_definition_arn" {
  value       = module.streaming_stack.ecs_task_definition_arn
  description = "ARN de la definición de tarea ECS"
}