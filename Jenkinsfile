node('docker') {
    stage ('lint') {
        checkout scm
        sh 'docker-compose run python'
        echo `which pylint`
        sh 'pylint app -f json > pylint_app.json'
        sh 'pylint pygoat -f json > pylint_pygoat.json'
        sh 'docker-compose down'
        }
    }
    stage('test') {
        sh 'docker-compose run python'
        sh 'python manage.py test app --settings=pygoat.docker_settings'

    }
    stage ('cleanup') {
         sh 'docker-compose down'
    }
}