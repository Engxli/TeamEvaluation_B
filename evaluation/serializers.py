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

        res = []
        teams = []
        judgeObjec = {}
        criteriaOfJudge = []
        for judge in obj.judge.all():
            judgeObjec = {"judge_id":judge.id,"judge_name": judge.name}
            for team in judge.grade:
                for criteria in team['grade']:
                    criteriaOfJudge.append({"criteria_id":criteria['criteria_id'], "criteria_name":criteria['criteria_name'], "criteria_weight":criteria['criteria_weight'], "criteria_score":criteria['grade']})                
                teams.append({**judgeObjec, "team_id":team['team_id'],"team_name":team['team_name'],"criteria":criteriaOfJudge})
                criteriaOfJudge=[]
            res.append(teams)
            teams=[]
        
        responseAttay = []
        responseObject = {}
        for judge in res:
            for team in judge:
                if team['team_id'] in responseObject.keys():
                    responseObject = {team['team_id']:{**responseObject[team['team_id']], "team_id":team['team_id'], "team_name":team['team_name']}}
                else:
                    responseObject = {**responseObject, team['team_id']:{ "team_id":team['team_id'], "team_name":team['team_name']}}
                for index,criteria in enumerate(team['criteria']):
                    if "criteria" in responseObject[team['team_id']].keys():
                        if {**criteria, "criteria_score":0} in [{**item, "criteria_score":0} for item in responseObject[team['team_id']]['criteria']]:
                            responseObject[team['team_id']]['criteria'][index]['criteria_score'].append(criteria['criteria_score'])
                        else:
                           responseObject[team['team_id']]['criteria'].append({**criteria, "criteria_score":[criteria['criteria_score']]}) 
                    else:
                        responseObject[team['team_id']]['criteria'] = [{**criteria, "criteria_score":[criteria['criteria_score']]}]
  
        return responseObject
        
