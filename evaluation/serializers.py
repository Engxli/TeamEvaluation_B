from rest_framework import serializers
from .models import Evaluation
from judge.serializers import JudgeSerializers

class EvaluationSerializers(serializers.ModelSerializer):
    judge = JudgeSerializers(many=True, read_only=True)
    avg = serializers.SerializerMethodField(method_name="get_avg")
    class Meta:
        model = Evaluation
        fields = "__all__"

    def get_avg(self, obj:Evaluation):
        data = []
        objactData = {}
        res = []
        for marker in obj.judge.all():
            for team in marker.grade:
                for criteria in team['grade']:
                    # print(criteria)
                    if criteria['criteria_id'] in objactData.keys():
                        objactData[criteria['criteria_id']]["grade"].append(criteria['grade'])
                    else:
                        objactData[criteria['criteria_id']] = {"judgeId": marker.id, "judgeName": marker.name}
                        objactData[criteria['criteria_id']] = {**objactData[criteria['criteria_id']],"criteriaID": criteria['criteria_id']}
                        objactData[criteria['criteria_id']] = {**objactData[criteria['criteria_id']], "criteriaName": criteria['criteria_name']}
                        objactData[criteria['criteria_id']] = {**objactData[criteria['criteria_id']], "criteriaWeight": criteria['criteria_weight']}
                        objactData[criteria['criteria_id']] = {**objactData[criteria['criteria_id']], "grade": [criteria['grade']]}
            data.append(objactData)
            objactData={}
        
        for marker in data:
            for key,value in marker.items():
                value['avgGrade'] = (sum(value['grade'])/len(value['grade']))*10
                res.append(value)
        
        return res
        
