db.createUser(
        {
                user: "consultaSQUAD",
                pwd: "consulta2413",
                roles: [
                        {
                                role: "readWrite",
                                db: "apisquad"
                        }
                ]
        }
)

db.createCollection("squadCollection")
