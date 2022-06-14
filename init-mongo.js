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
);

db.createCollection("squadCollection");
db.squadCollection.insert({_id: "itemId" , seqValue : 0 } );

function getSequenceNextValue(seqName) {
  var seqDoc = db.squadCollection.findAndModify({
    query: { _id: seqName },
    update: { $inc: { seqValue: 1 } },
    new: true
  });

 return seqDoc.seqValue;
}
