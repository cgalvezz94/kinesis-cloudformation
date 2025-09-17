terraform {
  backend "s3" {
    bucket          = "estado-kinesis-project"
    key             = "terraform.tfstate"
    region          = "us-east-1"
    dynamodb_table    = "terraform-lock"
  }
}