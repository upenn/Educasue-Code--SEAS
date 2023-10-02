import requests
import json
from config.config_vars import CANVAS_TOKEN

class Canvas:
    def __init__(self, instance):
        server_url = {'Production': 'https://canvas.your_institution.edu', 
                      'Test': 'https://your_institution.test.instructure.com'}

        self.instance = instance
        self.server_url = server_url[instance]
        self.access_token = self.get_token()

    def get_token(self=None):

        cred = CANVAS_TOKEN 

        return cred

    def headers(self):
        headers = {'Content-Type': 'application/json',
                    'Authorization': 'Bearer {}'.format(self.access_token)
        }
        
        return headers

    def post_assignment_grade(self, course_id, assignment_id, student_id, post_grade):

        assignment_grade = f'{self.server_url}/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}'

        playload = {'submission[posted_grade]': post_grade}

        r = requests.put(assignment_grade, headers=self.headers(), params=playload)

        if r.status_code == 200:
            return json.dumps(r.json(), indent=4)
        else:
            raise Exception(f'{r.status_code},{r.text}')
        
    def post_assignment_on_time(self, course_id, assignment_id, student_id):
        assignment_grade = f'{self.server_url}/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}'

        playload = {'submission[late_policy_status]': 'none'}

        r = requests.put(assignment_grade, headers=self.headers(), params=playload)

        if r.status_code == 200:
            return json.dumps(r.json(), indent=4)
        else:
            raise Exception(f'{r.status_code},{r.text}')

    def get_assignment_grades(self, course_id, assignment_id):

        student_grade = f'{self.server_url}/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions?per_page=100'

        r = requests.get(student_grade, headers=self.headers())

        raw  = r.json()

        data_set = []

        for question in raw:

            data_set.append(question)
        
        while r.links['current']['url'] != r.links['last']['url']:

            r = requests.get(r.links['next']['url'], headers=self.headers())

            raw = r.json()

            for question in raw:

                data_set.append(question)

        if r.status_code == 200:
            return data_set
        else:
            raise Exception(f'{r.status_code},{r.text}')
        
    def get_assignment_groups(self, course_id):

        assignment_groups = f'{self.server_url}/api/v1/courses/{course_id}/assignment_groups'


        playload = {'include[]': ['assignments']}

        r = requests.get(assignment_groups, headers=self.headers(), params=playload)

        raw = r.json()

        data_set = []

        for group in raw:

            data_set.append(group)
        
        while r.links['current']['url'] != r.links['last']['url']:

            r = requests.get(r.links['next']['url'], headers=self.headers())

            raw = r.json()

            for group in raw:

                data_set.append(group)


        if r.status_code == 200:
            return data_set
        else:
            raise Exception(f'{r.status_code},{r.text}')

    def get_assignment(self, course_id, assignment_id):

        assignmet_data = f'{self.server_url}/api/v1/courses/{course_id}/assignments/{assignment_id}/'

        r = requests.get(assignmet_data, headers=self.headers())

        raw  = r.json()

        if r.status_code == 200:
            return raw
        else:
            raise Exception(f'{r.status_code},{r.text}')

    def get_course(self, course_id):
            assignmet_data = f'{self.server_url}/api/v1/courses/{course_id}/'

            r = requests.get(assignmet_data, headers=self.headers())

            raw  = r.json()

            if r.status_code == 200:
                return raw
            else:
                raise Exception(f'{r.status_code},{r.text}')
