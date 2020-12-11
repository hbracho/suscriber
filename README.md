kubectl port-forward pod/mongodb-standalone-0  27017:27017 -n default
sudo mkdir k8-training


mongo mongodb://mongodb-standalone-0.database:27017
use training
db.auth('training','password')
show collections
db.suscribers.find()


My activities of the day.

    - Implment the methof get all suscribers=> Done
    - Implement the method delete a suscriber. => Done
    - implement the method get for a specific topic name with an attribute, this must have a suscriber. => Done.

    - encrypted the key => done.

    - topic is unique => done

    - cache => done.

    - create index  => done
        db.suscribers.createIndex({"topic_name":1},{unique: true })

    - invest in mongodb => pending
        quantity connextion available => acording the library have available 
            "connections":{
                "current":6,
                "available":838854,
                "totalCreated":222,
                "active":1
            },
        transcction => it isn't necesary (I am going to investigate a litle more)
        open close connection => library management it automatic.

    - Build the project in an architectura hexagonal => Donde
    - investigatea about max size cache by request flask


export HOST=localhost
export PORT=27017
export AUTHSOURCE=training
export USER_NAME=training
export DATABASE_NAME=training
export PASSWORD=password