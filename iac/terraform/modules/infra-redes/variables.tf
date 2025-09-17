variable "vpc_cidr" {
  type        = string
  description = "CIDR block para la VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  type        = string
  description = "CIDR block para la subnet pública"
  default     = "10.0.1.0/24"
}