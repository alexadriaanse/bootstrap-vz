def validate_manifest(data, validator, error):
	import os.path
	schema_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'manifest-schema.yml'))
	validator(data, schema_path)


def resolve_tasks(taskset, manifest):
	import tasks
	taskset.add(tasks.CheckAptProxy)
	taskset.add(tasks.SetAptProxy)
	if not manifest.plugins['apt_proxy'].get('persistent', False):
		taskset.add(tasks.RemoveAptProxy)
