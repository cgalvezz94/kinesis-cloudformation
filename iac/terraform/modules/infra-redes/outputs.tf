output "vpc_id" {
  description = "ID de la VPC principal"
  value       = aws_vpc.binance_vpc.id
}

output "public_subnet_id" {
  description = "Subnet pública para tareas ECS"
  value       = aws_subnet.binance_public_subnet.id
}

output "security_group_id" {
  description = "SG para tareas ECS"
  value       = aws_security_group.binance_sg.id
}