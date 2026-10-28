"""User-supplied storyboard/description reconstructions, not verbatim captions.

No frame-level timestamps were supplied. One whole-video segment records coverage,
not the time at which any individual statement was spoken.
"""
FALLBACKS = {
    'bsbWDqAXsrE': (339, """Controller Malia M. Cohen introduces ClaimIt.ca.gov and explains California Unclaimed Property Law. After three years of dormancy, covered property can include bank accounts, stocks, uncashed checks, insurance benefits, wages and safe deposit box contents. Real estate is excluded. Search by Last or Business Name, First Name and City or ZIP, or by Property ID. Active escheated properties have a +CLAIM button. Pre-escheat Notice properties have an INFO button showing holder contact information and a June 1 transfer deadline; an owner can contact the holder directly before transfer. Add multiple properties to the Claim Cart. Select the Claimant Relationship: Myself; Business Officer/Dissolving/LLC/Sole Prop; Heir; Heir-Trust; Heir-Will; Heir-Court Appointed Rep; Heir-Final Decree Distribution; Holder Reimbursement; Government Agency; or Bankruptcy Trustee. Complete the three-step eClaim form. Step 1 collects contact information, SSN and date of birth. Step 2 is an electronic signature under penalty of perjury. Step 3 presents a claim summary with Claim ID and a confirmation email within 24 hours. Upload verification documents through Upload Claim Documentation, with up to five files per batch in PDF, JPG or JPEG format, each between 1 KB and 15 MB. Document types include ID, SSN, Proof of Reported Address, Death Certificate, Trust/Will/Probate Decree and Investigator Agreement. Check status at ClaimIt.ca.gov or call 1-800-992-4647."""),
    'ZX-Ttx_4Ezo': (222, """The California State Controller's Office explains Property ID searching on ClaimIt.ca.gov. Do not use a middle initial on the initial search. The example John P Sullivan returns 73 matches while John Sullivan returns more than 500 because holders often omit middle initials. Last Name requires at least three characters. Narrow results with cities where the person lived or received mail. Holder reporting errors in names, streets, cities or ZIP codes can explain undelivered payments. Try partial city names, such as Gold for Gold River, common name misspellings, partial first names and nicknames, such as WIL for William or Will. Inspect results for former addresses, P.O. boxes and family members. Click Add beside a Property ID to add it to the Claims Cart, then Claim Properties in My Cart or Continue Search. File using eClaim or a paper mail-in form when complex heir documentation is required. Record the Property ID before calling (800) 992-4647."""),
    'MdSAG5LMn4I': (122, """Regrid demonstrates self-service acquisition of statewide standardized parcel data at store.regrid.com, covering more than 155 million US parcels. Select a state, such as Ohio with approximately 5.29 million parcels across 88 counties. Inspect the County Coverage Report spreadsheet and Parcel Schema / Data Dictionary. Fields and tier distinctions include APN, owner name, mailing address, situs address, land use, valuation, building footprints and secondary addresses, across Standard and Premium offerings. Add a statewide dataset to the cart, complete checkout under the Data License Agreement and download the full state bundle or individual county files. Available formats include CSV, GeoJSON, Shapefile (SHP), File Geodatabase (GDB), GeoPackage (GPKG) and KML. Support is available at parcels@regrid.com. This reconstruction combines the visual screen tutorial and video description; it is not a verbatim audio transcript."""),
}


def apply_storyboard_fallback(result):
    """Populate a known missing transcript without inventing word timestamps."""
    entry = FALLBACKS.get(result['video_id'])
    if entry is None:
        return False
    duration, text = entry
    result.update(status='ok', client='STORYBOARD_OCR', full_text=text,
                  selected_track=None,
                  segments=[{'start': 0.0, 'duration': float(duration), 'text': text,
                             'timing': 'whole_video_coverage_not_quote_timestamp'}],
                  provenance={'source': 'user_supplied_storyboard_and_description',
                              'verbatim': False, 'time_aligned': False,
                              'verification': 'User reported verified storyboard review; not independently re-OCRed.'})
    result.setdefault('metadata', {}).setdefault('lengthSeconds', str(duration))
    return True
