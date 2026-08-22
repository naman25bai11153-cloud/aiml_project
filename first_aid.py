FIRST_AID = {
    "choking": (
        "1. Encourage coughing.\n"
        "2. Lean the person forward and give 5 firm back blows.\n"
        "3. Give 5 upward abdominal thrusts (Heimlich maneuver).\n"
        "4. Repeat until the airway is clear."
    ),
    "bleeding": (
        "1. Apply direct, firm pressure with a clean cloth or gauze.\n"
        "2. Keep the injured area raised above heart level.\n"
        "3. Do NOT pull out deeply embedded objects; press around them."
    ),
    "cpr": (
        "1. Check for responsiveness and normal breathing.\n"
        "2. Push hard and fast in the center of the chest (100–120 bpm).\n"
        "3. If breathing returns, place them on their side (recovery position)."
    ),
    "burns": (
        "1. Hold the burn under cool running tap water for 10–20 minutes.\n"
        "2. Do NOT apply ice, oil, or butter.\n"
        "3. Cover loosely with a clean, dry cloth or plastic wrap."
    ),
    "fracture": (
        "1. Keep the limb still; do not try to realign the bone.\n"
        "2. Apply an ice pack wrapped in cloth to reduce swelling.\n"
        "3. Support the injured area with a splint or padding."
    ),
    "nosebleed": (
        "1. Sit upright and lean slightly forward (do NOT tilt head back).\n"
        "2. Pinch the soft part of the nose firmly for 10–15 minutes.\n"
        "3. Breathe through the mouth."
    ),
    "fainting": (
        "1. Lay the person flat on their back.\n"
        "2. Raise their legs about 12 inches off the ground.\n"
        "3. Loosen tight clothing and ensure fresh air flow."
    ),
    "heatstroke": (
        "1. Move to a cool, shaded, or air-conditioned area.\n"
        "2. Loosen clothing and apply cool, damp cloths to neck and armpits.\n"
        "3. Offer small sips of cool water only if fully conscious."
    ),
    "hypothermia": (
        "1. Move to a warm, dry area and remove wet clothing.\n"
        "2. Wrap in warm blankets covering the head and chest.\n"
        "3. Warm gradually; avoid direct intense heat."
    ),
    "seizure": (
        "1. Clear nearby sharp or hard objects; cushion the head.\n"
        "2. Do NOT hold the person down or put anything in their mouth.\n"
        "3. Roll them onto their side once shaking stops."
    ),
    "allergy": (
        "1. Help the person administer their auto-injector (EpiPen) if available.\n"
        "2. Keep them sitting upright to ease breathing.\n"
        "3. Loosen tight collar or clothing."
    ),
    "snake_bite": (
        "1. Keep the person calm and completely still to slow venom spread.\n"
        "2. Keep the bitten area at or below heart level.\n"
        "3. Do NOT cut the wound, apply ice, or suck the venom."
    ),
}
def aid():
    print("Enter the symptoms of your patient.")
    print("Type 'X' when finished to get first aid info.\n")

    symps = []
    n = 1
    while True:
        o = input(f"{n}: ").strip()
        if o.upper() == "X":
            break
        if o:  # Ignore empty presses
            symps.append(o.lower())
            n += 1

    print("\n--- FIRST AID PROCEDURES ---\n")
    for s in symps:
        if s in FIRST_AID:
            print(f"[{s}]:")
            print(FIRST_AID[s])
            print("-" * 30)
        else:
            print(
                f"[{s.upper()}]: Information for this symptom does not exist in our database.\n"
            )
