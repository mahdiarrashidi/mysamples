provider "aws" {
  region = "eu-west-2"
  access_key = "AAAAAAAAAA"
  secret_key = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
}

# ایجاد VPC
resource "aws_vpc" "example_vpc" {
  cidr_block       = "10.0.0.0/16"
 // availability_zone = "eu-west-2"
}

# ایجاد Subnet
resource "aws_subnet" "example_subnet" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.0.0/24"
  availability_zone = "eu-west-2a"
}

# ایجاد Security Group برای EC2 اول
resource "aws_security_group" "example_sg1" {
  name        = "example-sg1"
  description = "Security Group for EC2 Instance 1"
  vpc_id      = aws_vpc.example_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ایجاد Security Group برای EC2 دوم
resource "aws_security_group" "example_sg2" {
  name        = "example-sg2"
  description = "Security Group for EC2 Instance 2"
  vpc_id      = aws_vpc.example_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8
    to_port     = 8
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ایجاد EC2 Instance اول
resource "aws_instance" "example_instance1" {
  ami           = "ami-09744628bed84e434"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.example_subnet.id
  vpc_security_group_ids = [aws_security_group.example_sg1.id]
}

# ایجاد EC2 Instance دوم
resource "aws_instance" "example_instance2" {
  ami           = "ami-09744628bed84e434"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.example_subnet.id
  vpc_security_group_ids = [aws_security_group.example_sg2.id]
}
