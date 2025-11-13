import time
import json

from json_example import example_nested_json

class ObjectFromDict:
  @staticmethod
  def map_entry(entry):
    if isinstance(entry, dict):
      return ObjectFromDict(**entry)
    return entry

  def __init__(self, **kwargs):
    for key, val in kwargs.items():
      if type(val) == dict:
        setattr(self, key, ObjectFromDict(**val))
      elif type(val) == list:
        setattr(self, key, list(map(self.map_entry, val)))
      else:
        setattr(self, key, val)

TRIALS = 10000

dict_parse_times = []
obj_parse_times = []

for _ in range(TRIALS):
    pyd_start_time = time.perf_counter()
    dict_          = json.loads(example_nested_json)
    pyd_end_time   = time.perf_counter()
    dict_parse_times.append(pyd_end_time - pyd_start_time)


    obj_start_time = time.perf_counter()
    obj_           = ObjectFromDict(**dict_)
    obj_end_time   = time.perf_counter()
    obj_parse_times.append(obj_end_time - obj_start_time)

avg_dict_parse_time = sum(dict_parse_times) / TRIALS
avg_obj_parse_time = sum(obj_parse_times) / TRIALS
avg_total_parse_time = avg_dict_parse_time + avg_obj_parse_time

print()
print(f"Dictionary parsing time: {avg_dict_parse_time:.10f} seconds")
print(f"Object parsing time:     {avg_obj_parse_time:.10f} seconds\n")
print(f"Total parsing time:      {avg_total_parse_time:.10f} seconds\n")
print(f"Parsing with ObjectFromDict is ~{avg_total_parse_time / avg_dict_parse_time:.2f}x slower just parsing to dictionary.\n")