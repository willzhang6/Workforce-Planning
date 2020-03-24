import yaml
from TalentSystemSimulation import TalentSystemSimulation
config_file_path = "sim_config_1.yml"
with open(config_file_path, 'r') as config_file:
    sim_config = yaml.safe_load(config_file)
print(sim_config['eventPreditionModels']['attritionModel'])
talent_sys_sim = TalentSystemSimulation(sim_config)
