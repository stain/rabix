from os.path import dirname, join

from rabix.common.ref_resolver import from_url
from rabix.main import TEMPLATE_JOB
from rabix.main import dot_update_dict
from rabix.main import get_inputs_from_file


def test_remap_job():
    job = TEMPLATE_JOB
    tool = from_url(join(dirname(__file__), 'bwa-mem.json#tool'))
    input_file = from_url(join(dirname(__file__), 'inputs.json'))
    startdir = './'
    dot_update_dict(job['inputs'], get_inputs_from_file(tool, input_file, startdir)[
        'inputs'])
    print(job)

test_remap_job()