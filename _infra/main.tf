provider "aws" {
  region  = "us-west-2"
  profile = "personal"
}

terraform {
  backend "s3" {
    profile = "personal"
    bucket  = "colin-tfstate"
    key     = "colinfjw.tfstate.json"
    region  = "us-west-2"
  }
}
