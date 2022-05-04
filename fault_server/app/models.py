from graphene import ObjectType, String, Schema, List


class Fault(ObjectType):
    field_name = String()
    notes = String()


class FaultList(ObjectType):
    faults = List(String)


schema = Schema(query=Fault)
