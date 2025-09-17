resource "aws_kinesis_stream" "data_stream" {
  name                 = var.stream_name
  retention_period     = var.retention_hours
  stream_mode_details {
    stream_mode = var.stream_mode
  }
}

resource "aws_lambda_function" "stream_processor" {
  function_name = "StreamProcessor"
  runtime       = "python3.9"
  handler       = "lambda_handlers.kinesis_to_timestream.lambda_handler"
  role          = var.lambda_role_arn
  s3_bucket     = var.lambda_s3_bucket
  s3_key        = "kinesis_to_timestream.zip"
}

resource "aws_lambda_event_source_mapping" "kinesis_trigger" {
  event_source_arn  = aws_kinesis_stream.data_stream.arn
  function_name     = aws_lambda_function.stream_processor.arn
  starting_position = "LATEST"
}

resource "aws_grafana_workspace" "grafana" {
  account_access_type       = "CURRENT_ACCOUNT"
  authentication_providers  = ["AWS_SSO"]
  permission_type           = "SERVICE_MANAGED"
  name                      = "${var.project_name}-grafana"
  role_arn                  = var.grafana_role_arn
}

resource "aws_ecs_task_definition" "binance_task" {
  family                   = "binance-task"
  cpu                      = "256"
  memory                   = "512"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = var.ecs_task_role_arn

  container_definitions = jsonencode([
    {
      name      = "binance-container",
      image     = "public.ecr.aws/l1v8h9k1/binance-trades:latest",
      essential = true,
      logConfiguration = {
        logDriver = "awslogs",
        options = {
          awslogs-group         = var.log_group_name,
          awslogs-region        = "us-east-1",
          awslogs-stream-prefix = "binance"
        }
      }
    }
  ])
}