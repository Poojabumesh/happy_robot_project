from load_matcher import load_available

if __name__ == "__main__":
    results = load_available(
        "data/loads.csv", 
        origin="Dallas", 
        destination="Chicago", 
        equipment_type="Dry Van"
    )

    if results:
        print("✅ Matching loads found:")
        for load in results:
            print(load)
    else:
        print("❌ No matching loads.")
