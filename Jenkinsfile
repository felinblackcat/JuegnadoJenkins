node {
    stage("BuildTesting") {
        def customImage = docker.build("juegnadojenkins:latest")
        customImage.inside {
            sh "pytest --junitxml=./test.xml --cov=. --cov-fail-under=90 | grep TOTAL| awk '{ print \$4 }'"
        }
        sh "docker logs ${customImage.id}"
        
    }
    stage("CheckStaticCode") {
        echo "Hello, CheckStaticCode!"

    }
    stage("RunUnitaryTest") {
        echo "Hello, RunUnitaryTest!"
     }
    stage("BuildPreprod") {
        echo "Hello, BuildPreprod!"
    }
    stage("IntegrationTest") {
        echo "Hello, IntegrationTest!"
    }
    stage("CheckCVE") {
        echo "Hello, CheckCVE!"
    }
    stage("SendRegistry") {
        echo "Hello, SendRegistry!"

    }
    stage("UATDeploy") {
        echo "Hello, UAT Deploy!"
    }

}