# education/management/commands/load_resources.py

from django.core.management.base import BaseCommand
from education.models import Resource


class Command(BaseCommand):
    help = 'Create or update educational resources for various waste types.'

    def handle(self, *args, **kwargs):
        resources = [
            {
                "title": "Recycling Plastic Waste",
                "waste_type": "plastic",
                "category": "recycling",
                "recycling_process": "Sort plastics by type (e.g., PET, HDPE), remove contaminants, rinse thoroughly, and place in designated recycling bins.",
                "products_made": "Plastic bottles, fleece jackets, plastic lumber",
                "making_process": "To make a fleece jacket: Collect PET bottles, shred into flakes, melt and spin into polyester yarn, weave into fabric, and sew into jackets.",
                "tutorial_link": "https://youtu.be/Hf2Te2OsYqg?si=3l_hcUt9U3QzXTjp,https://youtu.be/cNPEH0GOhRw?si=xxBFKPFKfdR9g60H,https://youtu.be/obL-sTjn1Ok?si=lTi-aEQhIgzKs652,https://youtu.be/3KCfiiWGFxA?si=YWdVmo0xlLTww51A"
            },
            {
                "title": "Recycling Paper Waste",
                "waste_type": "paper",
                "category": "recycling",
                "recycling_process": "Collect paper waste, remove staples or tape, shred into pulp with water, filter to remove impurities, and press into new sheets.",
                "products_made": "New paper, cardboard, paper bags",
                "making_process": "To make recycled paper: Soak shredded paper in water, blend into pulp, spread onto a screen, press to remove water, and dry into sheets.",
                "tutorial_link": "https://youtu.be/5xrWrKIVBgo?si=dtxVfUdM6-0kwcuc"
            },
            {
                "title": "Recycling Glass Waste",
                "waste_type": "glass",
                "category": "recycling",
                "recycling_process": "Sort glass by color (clear, green, brown), remove caps or labels, crush into cullet, and send to a facility for melting and reshaping.",
                "products_made": "New glass bottles, fiberglass, glass beads",
                "making_process": "To make glass beads: Melt crushed glass at 1400°C, shape into beads using molds, cool slowly to avoid cracking.",
                "tutorial_link": "https://youtube.com/shorts/RBKk-RYMFVQ?si=avRIfOyZQO7kGpFp,https://youtu.be/b4Af2RATDLs?si=k62ChjZanKXrLI2y,https://youtu.be/Ow5LeG-zzyg?si=fgyx6_ki51kZJgmk,https://youtu.be/r15rHHnju4Y?si=Pew_LjEW46x1RALu,https://youtu.be/5xrWrKIVBgo?si=cUurQF_Elx-rrDq5"
            },
            {
                "title": "Composting Organic Waste",
                "waste_type": "organic",
                "category": "composting",
                "recycling_process": "Collect organic waste like fruit peels, vegetable scraps, and yard waste. Layer in a compost bin with dry materials (e.g., leaves), turn regularly, and keep moist. Compost is ready in 2-6 months.",
                "products_made": "Compost (soil enhancer), biogas",
                "making_process": "Compost is used directly as a soil enhancer. For biogas, organic waste is placed in an anaerobic digester to produce methane for energy.",
                "tutorial_link": "https://youtu.be/zy70DAaeFBI?si=oqqkvUk5gxFgJMmu"
            },
            {
                "title": "Recycling Metal Waste",
                "waste_type": "metal",
                "category": "recycling",
                "recycling_process": "Separate metals (e.g., aluminum, steel), clean to remove residues, shred into small pieces, and melt in a furnace for recasting.",
                "products_made": "New cans, car parts, construction materials",
                "making_process": "To make new cans: Melt aluminum at 660°C, pour into molds to form sheets, cut and shape into cans.",
                "tutorial_link": "https://youtu.be/_ErocQ2S080?si=1n5ngEHP_uRH75oi,https://youtu.be/UIPA-ZagWww?si=9mbZ72Adeyu9R84Q"
            },
            {
                "title": "Recycling E-Waste",
                "waste_type": "e-waste",
                "category": "recycling",
                "recycling_process": "Disassemble e-waste (e.g., computers, phones), separate components (plastics, metals, glass), shred materials, and use chemical processes to extract precious metals like gold and copper.",
                "products_made": "New electronics, jewelry, raw materials",
                "making_process": "Extracted gold can be refined and used in jewelry. The process involves chemical leaching and smelting, best done by professionals.",
                "tutorial_link": "https://youtu.be/U3KUJTDPsSE?si=cGo5bV5ByNAXPIU9,https://youtube.com/shorts/SKnX6ljFxB4?si=qpxL-kASIHTzGbho,https://youtu.be/vLpbQJehcrw?si=JNeljfpnEcKAmJsh"
            },
            {
                "title": "Recycling Clothing Waste",
                "waste_type": "clothing",
                "category": "recycling",
                "recycling_process": "Sort clothing by material (cotton, polyester), remove non-textile items, shred into fibers, and process into new textiles or insulation materials.",
                "products_made": "New fabrics, insulation, cleaning cloths",
                "making_process": "To make new fabrics: Clean and shred used clothing, spin fibers into yarn, weave into fabric on a loom.",
                "tutorial_link": "https://youtu.be/S67EG8ntlcM?si=9Ema-yjUcofyY5XX,https://youtu.be/yLZgrSpCAVs?si=EZw_uxEEKWT7oma3"
            },
            {
                "title": "Handling Hazardous Waste",
                "waste_type": "hazardous",
                "category": "disposal",
                "recycling_process": "Identify hazardous waste (e.g., batteries, chemicals), store safely in labeled containers, and deliver to authorized disposal facilities.",
                "products_made": "Some materials can be processed into industrial chemicals or energy",
                "making_process": "Processing involves neutralization or incineration, typically done by professionals.",
                "tutorial_link": "https://youtu.be/MJX0rvGsRpA?si=48BxgNRw3cIK8Vgc,https://youtu.be/aPML7f2KM8g?si=6uFoZGwauL9yuPEz"
            },
            {
                "title": "Recycling Construction Waste",
                "waste_type": "construction",
                "category": "recycling",
                "recycling_process": "Sort materials (e.g., concrete, wood, metal), crush concrete into aggregate, repurpose wood, and recycle metals.",
                "products_made": "Recycled concrete aggregate, reclaimed wood furniture, new metal products",
                "making_process": "To make recycled concrete aggregate: Crush concrete debris, screen for size, use as a base for new construction.",
                "tutorial_link": "https://youtube.com/shorts/aH-s4D6Q8lQ?si=2wROEFRcmZi9D4QX,https://youtu.be/_ctiJ4nUXrs?si=GLIHaHbotvIzhiY8"
            },
            {
                "title": "Managing Medical Waste",
                "waste_type": "medical",
                "category": "disposal",
                "recycling_process": "Segregate medical waste (e.g., sharps, infectious waste), use autoclaving or incineration, and dispose of in regulated facilities.",
                "products_made": "Some plastics can be recycled into non-medical products like benches",
                "making_process": "Recycled plastics are melted and molded into new products, done by specialized facilities.",
                "tutorial_link": "https://youtu.be/IxbHoDHzypI?si=B8GGjJxmh3xpQPso"
            },
        ]

        for data in resources:
            resource, created = Resource.objects.update_or_create(
                waste_type=data["waste_type"],
                defaults=data
            )
            status = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{status} resource for: {data['waste_type']}"))
