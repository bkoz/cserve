# Deploy cserve on Openshift

#### Generate a pull token

#### Create an Openshift pull secret
```bash
oc create secret generic centmldockerpull --from-file=.dockerconfigjson=./dockerconfig.json --type=kubernetes.io/dockerconfigjson
```

#### Run the cserve helm chart

#### Test using `curl`.

```bash
export CSERVE_HOST=http://cserve:8080

curl -H 'Content-Type: application/json' $CSERVE_HOST/openai/v1/models | jq

curl -N -X POST  -H 'Content-Type: application/json' $CSERVE_HOST/cserve/v1/generate -d '{"prompt": "What is a large language model? ", "sampling_params": {"n": 1, "temperature": 0, "max_tokens": 1024}, "stream": true}'
```

#### Deploy the example chat client on Openshift

```bash
oc new-app https://github.com/bkoz/cserve.git
```

