from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from .models import Evaluation
from judge.serializers import JudgeSerializers
class EvaluationSerializers(serializers.ModelSerializer):
    judge = JudgeSerializers(many=True, read_only=True)
    # avg = serializers.SerializerMethodField(method_name="get_avg")
    class Meta:
        model = Evaluation
        fields = "__all__"
    def get_avg(self, obj:Evaluation):
        data = []
        objactData = {}

        for judge in judge:
            objactData['judge'] = {'id':judge['id'],"name":judge['name'], "grades":{}}
            readGrade = {}
            for teams in judge['grade']:
                grades = [{grade['criteria_id']:grade['grade'] } for grade in teams['grade']]
                print(grades)
                for key in grades.key():
                    readGrade[key]=[]
                print(readGrade)

                    


                    # print(objactData["judge"]["grades"].keys())
                    # print(grade['criteria_id'])
                    # print(objactData["judge"]["grades"].keys())
                    # objactData["judge"]["grades"][grade['criteria_id']] = 1
                    # print(objactData["judge"]["grades"][grade['criteria_id']])
                    # # objactData["judge"]["grades"][grade['criteria_id']] =  [grade['criteria_weight']]
                    # if grade['criteria_id'] in objactData["judge"]["grades"].keys():
                    #     print("true")
                    #     objactData["judge"]["grades"][grade['criteria_id']].append(grade['criteria_weight'])
                    # else:
                    #     objactData["judge"]["grades"][grade['criteria_id']] =  [grade['criteria_weight']]
                    #     print(objactData)


            data.append(objactData)
                     # print(grade['criteria_id'])
                    # objactData["judge"]["grades"].append({grade['criteria_id']:grade['criteria_weight']})



        # data["total_judge"] = len(obj.judge.all())
        # data['criteria'] = []

        # for judge in obj.judge.all():
        #     for teams in judge['grade'].all():
        #         data['criteria'].append({judge['name']:[]})
        #         for grade in teams['grade'].all():
        #             data['criteria'][]
        pass