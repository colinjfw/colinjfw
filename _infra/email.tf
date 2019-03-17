module "emails" {
  source = "github.com/ColDog/ses-email-forwarder"

  # Name to prefix all resources.
  name = "colinjfw-email"

  # SES approved domain to send from.
  from_email = "noreply@colinjfw.com"

  # A list of recipients to receive. This is sent to the SES rule.
  recipients = ["colinjfw.com"]

  # Specify a mapping to forward to:
  mapping = {
    "@colinjfw.com" = ["colinwalker270@gmail.com"]
  }
}
