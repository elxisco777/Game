from pymongo import MongoClient
import json

class DatabaseManager:
    def __init__(self, db_name):
        self.db_client = MongoClient(db_name).test

    def insert_enpleadoselectronica(self, empleados):
        self.db_client.tiendas.insert_many(empleados)

empleados = []
pathBBDD = "mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"


empleados = [
{
    "id": {"$numberInt":"3"},
    "nombre_tienda": "HortiMarket",
    "nombre_ciudad": "Utiel",
    "tamano": {"$numberInt":"22"},
    "precio": {"$numberLong":"44000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.56947922109916"},
    "coordenadas_y": {"$numberDouble":"-1.2074049047190556"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores del Campo",
    "nombre_ciudad": "Utiel",
    "tamano": {"$numberInt":"35"},
    "precio": {"$numberLong":"70000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.57284592745865"},
    "coordenadas_y": {"$numberDouble":"-1.2105070024965403"}
  },
    {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Novelda",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.384992"},
    "coordenadas_y": {"$numberDouble":"-0.767652"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "TierraFértil",
    "nombre_ciudad": "Novelda",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.384342"},
    "coordenadas_y": {"$numberDouble":"-0.766452"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Agricultura Viva",
    "nombre_ciudad": "Novelda",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.383692"},
    "coordenadas_y": {"$numberDouble":"-0.765252"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "Novelda",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.383042"},
    "coordenadas_y": {"$numberDouble":"-0.764052"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Novelda",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.382392"},
    "coordenadas_y": {"$numberDouble":"-0.762852"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Jumilla",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.480492"},
    "coordenadas_y": {"$numberDouble":"-1.325652"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "TierraFértil",
    "nombre_ciudad": "Jumilla",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.481492"},
    "coordenadas_y": {"$numberDouble":"-1.326652"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "HortiMarket",
    "nombre_ciudad": "Jumilla",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.482492"},
    "coordenadas_y": {"$numberDouble":"-1.327652"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Jumilla",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.483492"},
    "coordenadas_y": {"$numberDouble":"-1.328652"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Jumilla",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.484492"},
    "coordenadas_y": {"$numberDouble":"-1.329652"}
  },
    {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Baeza",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.995519"},
    "coordenadas_y": {"$numberDouble":"-3.468163"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "VerdeValle",
    "nombre_ciudad": "Baeza",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.996519"},
    "coordenadas_y": {"$numberDouble":"-3.469163"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Baeza",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.997519"},
    "coordenadas_y": {"$numberDouble":"-3.470163"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Cosechas del Campo",
    "nombre_ciudad": "Baeza",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.998519"},
    "coordenadas_y": {"$numberDouble":"-3.471163"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Baeza",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.999519"},
    "coordenadas_y": {"$numberDouble":"-3.472163"}
  },
    {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "CampoFresco",
    "nombre_ciudad": "Ulldecona",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.577019"},
    "coordenadas_y": {"$numberDouble":"0.589076"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Ulldecona",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.578019"},
    "coordenadas_y": {"$numberDouble":"0.590076"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Ulldecona",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.579019"},
    "coordenadas_y": {"$numberDouble":"0.591076"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "Ulldecona",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.580019"},
    "coordenadas_y": {"$numberDouble":"0.592076"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Ulldecona",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.581019"},
    "coordenadas_y": {"$numberDouble":"0.593076"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "CampoFresco",
    "nombre_ciudad": "La Roda",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.216832"},
    "coordenadas_y": {"$numberDouble":"-2.148982"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "La Roda",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.217832"},
    "coordenadas_y": {"$numberDouble":"-2.149982"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "La Roda",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.218832"},
    "coordenadas_y": {"$numberDouble":"-2.150982"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "La Roda",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.219832"},
    "coordenadas_y": {"$numberDouble":"-2.151982"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "La Roda",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.220832"},
    "coordenadas_y": {"$numberDouble":"-2.152982"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "CampoFresco",
    "nombre_ciudad": "Tazacorte",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"28.635426"},
    "coordenadas_y": {"$numberDouble":"-17.932030"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "VerdeValle",
    "nombre_ciudad": "Tazacorte",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"28.636426"},
    "coordenadas_y": {"$numberDouble":"-17.933030"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "HortiMarket",
    "nombre_ciudad": "Tazacorte",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"28.637426"},
    "coordenadas_y": {"$numberDouble":"-17.934030"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Cosechas del Campo",
    "nombre_ciudad": "Tazacorte",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"28.638426"},
    "coordenadas_y": {"$numberDouble":"-17.935030"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Tazacorte",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"28.639426"},
    "coordenadas_y": {"$numberDouble":"-17.936030"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "CampoFresco",
    "nombre_ciudad": "Calahorra",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.308045"},
    "coordenadas_y": {"$numberDouble":"-1.964360"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Calahorra",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.309045"},
    "coordenadas_y": {"$numberDouble":"-1.965360"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "TierraFecunda",
    "nombre_ciudad": "Calahorra",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.310045"},
    "coordenadas_y": {"$numberDouble":"-1.966360"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "Calahorra",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.311045"},
    "coordenadas_y": {"$numberDouble":"-1.967360"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Calahorra",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.312045"},
    "coordenadas_y": {"$numberDouble":"-1.968360"}
  },
    {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "CampoFresco",
    "nombre_ciudad": "Reus",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.156689"},
    "coordenadas_y": {"$numberDouble":"1.106464"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Reus",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.157689"},
    "coordenadas_y": {"$numberDouble":"1.107464"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Reus",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.158689"},
    "coordenadas_y": {"$numberDouble":"1.108464"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Reus",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.159689"},
    "coordenadas_y": {"$numberDouble":"1.109464"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Reus",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.160689"},
    "coordenadas_y": {"$numberDouble":"1.110464"}
  },
    {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Tordesillas",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.502591"},
    "coordenadas_y": {"$numberDouble":"-4.937301"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "VerdeValle",
    "nombre_ciudad": "Tordesillas",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.503591"},
    "coordenadas_y": {"$numberDouble":"-4.938301"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "TierraFecunda",
    "nombre_ciudad": "Tordesillas",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.504591"},
    "coordenadas_y": {"$numberDouble":"-4.939301"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "AgroProductos Selectos",
    "nombre_ciudad": "Tordesillas",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.505591"},
    "coordenadas_y": {"$numberDouble":"-4.940301"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Tordesillas",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.506591"},
    "coordenadas_y": {"$numberDouble":"-4.941301"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "El Ejido",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"36.771322"},
    "coordenadas_y": {"$numberDouble":"-2.813672"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "El Ejido",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"36.772322"},
    "coordenadas_y": {"$numberDouble":"-2.814672"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "El Ejido",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"36.773322"},
    "coordenadas_y": {"$numberDouble":"-2.815672"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "El Ejido",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"36.774322"},
    "coordenadas_y": {"$numberDouble":"-2.816672"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "El Ejido",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"36.775322"},
    "coordenadas_y": {"$numberDouble":"-2.817672"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Lepe",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.257193"},
    "coordenadas_y": {"$numberDouble":"-7.208122"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Lepe",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.258193"},
    "coordenadas_y": {"$numberDouble":"-7.209122"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Campo y Cultivo",
    "nombre_ciudad": "Lepe",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.259193"},
    "coordenadas_y": {"$numberDouble":"-7.210122"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Lepe",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.260193"},
    "coordenadas_y": {"$numberDouble":"-7.211122"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Lepe",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.261193"},
    "coordenadas_y": {"$numberDouble":"-7.212122"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Cieza",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.239841"},
    "coordenadas_y": {"$numberDouble":"-1.416097"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "VerdeValle",
    "nombre_ciudad": "Cieza",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.240841"},
    "coordenadas_y": {"$numberDouble":"-1.417097"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "GreenHarvest",
    "nombre_ciudad": "Cieza",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.241841"},
    "coordenadas_y": {"$numberDouble":"-1.418097"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Cieza",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.242841"},
    "coordenadas_y": {"$numberDouble":"-1.419097"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Cieza",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.243841"},
    "coordenadas_y": {"$numberDouble":"-1.420097"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Mazarrón",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.573301"},
    "coordenadas_y": {"$numberDouble":"-1.308769"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "GranjaViva",
    "nombre_ciudad": "Mazarrón",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.574301"},
    "coordenadas_y": {"$numberDouble":"-1.309769"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Campo y Cultivo",
    "nombre_ciudad": "Mazarrón",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.575301"},
    "coordenadas_y": {"$numberDouble":"-1.310769"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Mazarrón",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.576301"},
    "coordenadas_y": {"$numberDouble":"-1.311769"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Agrícola Natural",
    "nombre_ciudad": "Mazarrón",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.577301"},
    "coordenadas_y": {"$numberDouble":"-1.312769"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Burriana",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.888052"},
    "coordenadas_y": {"$numberDouble":"0.091331"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Burriana",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.888152"},
    "coordenadas_y": {"$numberDouble":"0.091431"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Burriana",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.888252"},
    "coordenadas_y": {"$numberDouble":"0.091531"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "Burriana",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.888352"},
    "coordenadas_y": {"$numberDouble":"0.091631"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Burriana",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.888452"},
    "coordenadas_y": {"$numberDouble":"0.091731"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Carcaixent",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.121502"},
    "coordenadas_y": {"$numberDouble":"-0.469780"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "GranjaViva",
    "nombre_ciudad": "Carcaixent",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.121602"},
    "coordenadas_y": {"$numberDouble":"-0.469880"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "GreenHarvest",
    "nombre_ciudad": "Carcaixent",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.121702"},
    "coordenadas_y": {"$numberDouble":"-0.469980"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Carcaixent",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.121802"},
    "coordenadas_y": {"$numberDouble":"-0.470080"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Carcaixent",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"39.121902"},
    "coordenadas_y": {"$numberDouble":"-0.470180"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Caravaca de la Cruz",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.099496"},
    "coordenadas_y": {"$numberDouble":"-1.856620"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Caravaca de la Cruz",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.099596"},
    "coordenadas_y": {"$numberDouble":"-1.856720"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Caravaca de la Cruz",
    "tamano": {"$numberInt":"80"},
    "precio": {"$numberLong":"160000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.099696"},
    "coordenadas_y": {"$numberDouble":"-1.856820"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Caravaca de la Cruz",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.099796"},
    "coordenadas_y": {"$numberDouble":"-1.856920"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Caravaca de la Cruz",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"38.099896"},
    "coordenadas_y": {"$numberDouble":"-1.857020"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Palencia",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"80000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.004347"},
    "coordenadas_y": {"$numberDouble":"-4.530055"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "GranjaViva",
    "nombre_ciudad": "Palencia",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"60000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.005347"},
    "coordenadas_y": {"$numberDouble":"-4.531055"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Campo y Cultivo",
    "nombre_ciudad": "Palencia",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"120000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.006347"},
    "coordenadas_y": {"$numberDouble":"-4.532055"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Palencia",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"100000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.007347"},
    "coordenadas_y": {"$numberDouble":"-4.533055"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Agrícola Natural",
    "nombre_ciudad": "Palencia",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"140000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"42.008347"},
    "coordenadas_y": {"$numberDouble":"-4.534055"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Soto del Real",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"88000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.840568"},
    "coordenadas_y": {"$numberDouble":"-3.753581"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Soto del Real",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"66000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.839681"},
    "coordenadas_y": {"$numberDouble":"-3.753234"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Soto del Real",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"132000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.838917"},
    "coordenadas_y": {"$numberDouble":"-3.754183"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "TierraFresca",
    "nombre_ciudad": "Soto del Real",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"110000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.839321"},
    "coordenadas_y": {"$numberDouble":"-3.754817"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Soto del Real",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"154000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.840047"},
    "coordenadas_y": {"$numberDouble":"-3.754950"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "AgroTienda Verde",
    "nombre_ciudad": "Girona",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"88000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.981697"},
    "coordenadas_y": {"$numberDouble":"2.819556"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "Sabor Fresco",
    "nombre_ciudad": "Girona",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"66000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.982168"},
    "coordenadas_y": {"$numberDouble":"2.818717"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "GreenHarvest",
    "nombre_ciudad": "Girona",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"132000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.982761"},
    "coordenadas_y": {"$numberDouble":"2.818243"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Cosechas del Campo",
    "nombre_ciudad": "Girona",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"110000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.982464"},
    "coordenadas_y": {"$numberDouble":"2.819389"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Girona",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"154000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"41.983072"},
    "coordenadas_y": {"$numberDouble":"2.818989"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Tortosa",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"66000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.814711"},
    "coordenadas_y": {"$numberDouble":"0.521081"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "GranjaViva",
    "nombre_ciudad": "Tortosa",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"88000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.813782"},
    "coordenadas_y": {"$numberDouble":"0.520934"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Agricultura Viva",
    "nombre_ciudad": "Tortosa",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"132000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.812951"},
    "coordenadas_y": {"$numberDouble":"0.520734"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Tortosa",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"110000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.812208"},
    "coordenadas_y": {"$numberDouble":"0.520557"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Raíces Verdes",
    "nombre_ciudad": "Tortosa",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"154000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.811489"},
    "coordenadas_y": {"$numberDouble":"0.520397"}
  },
   {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Baza",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"66000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.491918"},
    "coordenadas_y": {"$numberDouble":"-2.775285"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "TierraFértil",
    "nombre_ciudad": "Baza",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"88000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.491202"},
    "coordenadas_y": {"$numberDouble":"-2.774978"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "EcoGusto",
    "nombre_ciudad": "Baza",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"132000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.490505"},
    "coordenadas_y": {"$numberDouble":"-2.774678"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Cosechas del Campo",
    "nombre_ciudad": "Baza",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"110000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.489808"},
    "coordenadas_y": {"$numberDouble":"-2.774378"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Agrícola Natural",
    "nombre_ciudad": "Baza",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"154000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"37.489111"},
    "coordenadas_y": {"$numberDouble":"-2.774078"}
  },
  {
    "id": {"$numberInt":"1"},
    "nombre_tienda": "Delicias Naturales",
    "nombre_ciudad": "Candeleda",
    "tamano": {"$numberInt":"30"},
    "precio": {"$numberLong":"66000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.140094"},
    "coordenadas_y": {"$numberDouble":"-5.273237"}
  },
  {
    "id": {"$numberInt":"2"},
    "nombre_tienda": "TierraFértil",
    "nombre_ciudad": "Candeleda",
    "tamano": {"$numberInt":"40"},
    "precio": {"$numberLong":"88000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.139498"},
    "coordenadas_y": {"$numberDouble":"-5.273974"}
  },
  {
    "id": {"$numberInt":"3"},
    "nombre_tienda": "Campo y Cultivo",
    "nombre_ciudad": "Candeleda",
    "tamano": {"$numberInt":"60"},
    "precio": {"$numberLong":"132000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.139016"},
    "coordenadas_y": {"$numberDouble":"-5.274675"}
  },
  {
    "id": {"$numberInt":"4"},
    "nombre_tienda": "Sabores de la Tierra",
    "nombre_ciudad": "Candeleda",
    "tamano": {"$numberInt":"50"},
    "precio": {"$numberLong":"110000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.138402"},
    "coordenadas_y": {"$numberDouble":"-5.274295"}
  },
  {
    "id": {"$numberInt":"5"},
    "nombre_tienda": "Frescura Natural",
    "nombre_ciudad": "Candeleda",
    "tamano": {"$numberInt":"70"},
    "precio": {"$numberLong":"154000"},
    "propietario": "Libre",
    "coordenadas_x": {"$numberDouble":"40.138012"},
    "coordenadas_y": {"$numberDouble":"-5.273682"}
  }
    ]
db = DatabaseManager(pathBBDD)
db.insert_enpleadoselectronica(empleados)
