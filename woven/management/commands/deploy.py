#!/usr/bin/env python
from optparse import make_option

from woven.main import deploy, activate
from woven.management.base import WovenCommand
from woven.utils import set_project_env

class Command(WovenCommand):

    help = "Deploy the current version of your project"
    requires_model_validation = False
    
    def handle_host(self,*args, **options):
        set_project_env()
        deploy()
        activate()

