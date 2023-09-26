import os
from scratchclient import ScratchSession

password = os.environ.get("SCRATCH_PASSWORD")

with open('description.txt', 'r') as file:
    description = file.read()

session = ScratchSession("Ieahcimto", password)
session.get_studio(33916577).set_description(description)
