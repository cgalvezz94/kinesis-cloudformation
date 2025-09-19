output "lambda_function_name" {
  value       = module.infra-secundaria.lambda_function_name
  description = "Nombre de la función Lambda"
}

output "grafana_workspace_id" {
  value       = module.infra-secundaria.grafana_workspace_id
  description = "ID del workspace de Grafana"
}

output "ecs_task_definition_arn" {
  value       = module.infra-secundaria.ecs_task_definition_arn
  description = "ARN de la definición de tarea ECS"
}