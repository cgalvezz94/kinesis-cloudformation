resource "aws_s3_bucket" "lambda_bucket" {
  bucket = var.bucket_name
}

resource "aws_ecs_cluster" "binance_cluster" {
  name = "binance-cluster"
}

resource "aws_iam_role" "lambda_role" {
  name = "LambdaKinesisTimestreamRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "lambda.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_role_attachments" {
  for_each   = var.managed_policy_arns_lambda_role
  role       = aws_iam_role.lambda_role.name
  policy_arn = each.value
}



resource "aws_iam_role" "grafana_role" {
  name = "GrafanaRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "grafana.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "grafana_role_attachments" {
  for_each   = var.managed_policy_arns_grafana_role
  role       = aws_iam_role.grafana_role.name
  policy_arn = each.value
}

resource "aws_iam_role" "ecs_role" {
  name = "binance-task-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "ecs-tasks.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
  tags = {
    Name = "binance-task-execution-role"
  }
}

resource "aws_iam_role_policy_attachment" "ecs_role_attachments" {
  for_each   = var.managed_policy_arns_ecs_role
  role       = aws_iam_role.ecs_role.name
  policy_arn = each.value
}

resource "aws_cloudwatch_log_group" "binance_log_group" {
  name              = "/ecs/binance-trades"
  retention_in_days = 7
  tags = {
    Name = "binance-log-group"
  }
}

data "aws_caller_identity" "current" {}