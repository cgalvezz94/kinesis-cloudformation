resource "aws_vpc" "binance_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "binance-vpc"
  }
}

resource "aws_internet_gateway" "binance_igw" {
  tags = {
    Name = "binance-igw"
  }
}

resource "aws_internet_gateway_attachment" "binance_igw_attachment" {
  vpc_id             = aws_vpc.binance_vpc.id
  internet_gateway_id = aws_internet_gateway.binance_igw.id
}

resource "aws_subnet" "binance_public_subnet" {
  vpc_id                  = aws_vpc.binance_vpc.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true
  availability_zone       = data.aws_availability_zones.available.names[0]
  tags = {
    Name = "binance-public-subnet"
  }
}

resource "aws_route_table" "binance_route_table" {
  vpc_id = aws_vpc.binance_vpc.id
  tags = {
    Name = "binance-route-table"
  }
}

resource "aws_route" "binance_route" {
  route_table_id         = aws_route_table.binance_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.binance_igw.id
}

resource "aws_route_table_association" "binance_subnet_association" {
  subnet_id      = aws_subnet.binance_public_subnet.id
  route_table_id = aws_route_table.binance_route_table.id
}

resource "aws_security_group" "binance_sg" {
  name        = "binance-sg"
  description = "Access for ECS Fargate tasks"
  vpc_id      = aws_vpc.binance_vpc.id

  ingress {
      description      = "Allow HTTPS"
      from_port        = 443
      to_port          = 443
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
      description      = "Allow HTTP"
      from_port        = 80
      to_port          = 80
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "binance-sg"
  }
}

data "aws_availability_zones" "available" {}