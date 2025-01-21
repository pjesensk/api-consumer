import groovy.json.JsonOutput
jenkins = Jenkins.instance
results = []
for (job in jenkins.getAllItems(Job.class)) {
   for(Run run in job.getBuilds()){
     results.add ([
        time: run.getTimeInMillis(),
        org: run.toString().split('/')[0],
        result: run.getResult(),
	    job: job.name,
       	run: run.toString(),
     ])    
   }
 }
println ( JsonOutput.toJson(results))
